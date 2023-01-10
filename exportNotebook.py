import nbformat
import os

from nbconvert.exporters import MarkdownExporter
from nbconvert.preprocessors import Preprocessor

from ipython_genutils.ipstruct import Struct

from traitlets.config import Config

from binascii import a2b_base64

class exportImageAttachments(Preprocessor):
    def processAttachment(self, inputData, index, attachmentIndex, output_files_dir, extension):
        data = a2b_base64(inputData)
        filename = "cell-" + str(index) + "-" + str(attachmentIndex) + extension
        if output_files_dir is not None:
            filename = os.path.join(output_files_dir, filename)
        return filename, data

    def preprocess_cell(self, cell, resources, index):
        output_files_dir = resources.get('output_files_dir', None)
        attachments = getattr(cell, 'attachments', Struct())
        if len(attachments) > 0:
            for attachmentIndex, attachment in enumerate(attachments):
                filename = None
                data = None
                if "image/png" in attachments[attachment].keys():
                    filename, data = self.processAttachment(attachments[attachment]["image/png"], index, attachmentIndex, output_files_dir, ".png")
                    resources["outputs"][filename] = data
                elif "image/jpeg" in attachments[attachment].keys():
                    filename, data = self.processAttachment(attachments[attachment]["image/jpeg"], index, attachmentIndex, output_files_dir, ".jpeg")
                    resources["outputs"][filename] = data
                oldName = "attachment:" + attachment
                cell.source = cell.source.replace(oldName, filename)
        return cell, resources

def exportNotebook(notebookFile, outputDirectory):
    exporterConfig = Config()
    exporterConfig.MarkdownExporter.preprocessors = [exportImageAttachments]

    notebookRaw = open(notebookFile).read()
    notebook = nbformat.reads(notebookRaw, as_version=4)

    markdown_exporter = MarkdownExporter(config=exporterConfig)
    (body, resources) = markdown_exporter.from_notebook_node(notebook)

    #save files
    outputFile = os.path.join(outputDirectory,os.path.basename(notebookFile).replace(".ipynb", ".md"))
    with open(outputFile, "w") as notebookOutput:
        notebookOutput.write(body)
    for resource in resources["outputs"]:
        with open(outputDirectory + "/" + resource, "wb") as imageOutput:
            imageOutput.write(resources["outputs"][resource])
