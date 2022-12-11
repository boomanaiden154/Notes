import sys
import json
import os
import shutil
import subprocess
import exportNotebook

from airium import Airium

outputLocation = "./build"

if not os.path.exists(outputLocation):
    os.makedirs(outputLocation)

def generateSite(siteConfig):
    site = Airium()
    site("<!DOCTYPE html>")

    if not os.path.exists(outputLocation + "/" + siteConfig["stylesheet"]):
        shutil.copyfile(siteConfig["stylesheet"], outputLocation + "/" + siteConfig["stylesheet"])

    with site.html():
        site.title(_t=siteConfig["title"])
        site.link(rel="stylesheet",href=siteConfig["stylesheet"])
        site.meta(name="viewport",content="width=device-width, initial-scale=1.0")

        #site header
        with site.div(klass="indent1"):
            with site.h1():
                site(siteConfig["title"])

        for category in siteConfig["categories"]:
            with site.div(klass="indent1"):
                with site.h2():
                    site(category["name"])
                for link in category["links"]:
                    with site.a(href=processLink(link)):
                        site(link["text"])
                    site.br()

    outputFileLocation = siteConfig["name"] + ".html"
    with open(outputLocation + "/" + outputFileLocation, "w") as outputFile:
        outputFile.write(str(site))

    return outputFileLocation

def processLink(linkObject):
    if "depends" in linkObject:
        for dependency in linkObject["depends"]:
            outputDependLocation = os.path.join(outputLocation, dependency["file"])
            if not os.path.exists(os.path.dirname(outputDependLocation)):
                os.makedirs(os.path.dirname(outputDependLocation))
            shutil.copy(dependency["file"], outputDependLocation)

    match linkObject["type"]:
        case "markdown":
            return processMarkdown(linkObject)
        case "static":
            return processStatic(linkObject)
        case "jupyter":
            return processJupyter(linkObject)
        case "subsite":
            with open(linkObject["file"]) as subsiteConfigFile:
                subsiteConfig = json.load(subsiteConfigFile)
                return generateSite(subsiteConfig)

def processMarkdown(linkObject):
    outputHTML = os.path.splitext(linkObject["file"])[0] + ".html"
    outputPath = os.path.join(outputLocation, outputHTML)
    if not os.path.exists(os.path.dirname(outputPath)):
        os.makedirs(os.path.dirname(outputPath))
    commandVector = ["pandoc", "--mathjax", "-s", linkObject["file"], "-F", "mermaid-filter", "-o", outputPath]
    process = subprocess.Popen(commandVector)
    process.wait()
    return outputHTML

def processStatic(linkObject):
    outputPath = os.path.join(outputLocation, linkObject["file"])
    if not os.path.exists(os.path.dirname(outputPath)):
        os.makedirs(os.path.dirname(outputPath))
    shutil.copy(linkObject["file"], outputPath)
    return linkObject["file"]

def processJupyter(linkObject):
    outputDirectory = os.path.dirname(linkObject["file"])
    outputDirectory = os.path.join(outputDirectory, os.path.basename(linkObject["file"]).replace(".ipynb","/"))
    outputPath = os.path.join(outputLocation, outputDirectory)
    if not os.path.exists(os.path.dirname(outputPath)):
        os.makedirs(outputPath)
    print(outputDirectory)
    print(outputPath)
    exportNotebook.exportNotebook(linkObject["file"], outputPath)
    exportedMarkdown = os.path.join(outputPath, os.path.basename(linkObject["file"]).replace("ipynb", "md"))
    outputHTMLPath = os.path.join(outputPath, os.path.basename(linkObject["file"]).replace("ipynb", "html"))
    commandVector = ["pandoc", "--mathjax", "-s", exportedMarkdown, "-o", outputHTMLPath]
    process = subprocess.Popen(commandVector)
    process.wait()
    os.remove(exportedMarkdown)
    outputHTML = os.path.join(outputDirectory, os.path.basename(linkObject["file"]).replace("ipynb","html"))
    return outputHTML

if __name__ == "__main__":
    with open("index.json") as indexFile:
        index = json.load(indexFile)
        generateSite(index)
