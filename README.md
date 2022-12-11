# Notes

This project contains a collection of (bad) notes and ramblings that get
published to my website at [aidengrossman.com](https://aidengrossman.com).
This public Github mirror accepts contributions and allows other people
to collaborate on notes and fix the numerous mistakes that are present
within the repository.

### Getting Started

To get started, first off you need to clone the repository:

```
git clone https://github.com/boomanaiden154/Notes
```

Then you can start modifying existing content, or adding new static content
such as Jupyter notebooks or markdown. If you've just changed content, you
can go ahead and open up a pull request to get the changes pushed upstream.
If you've added new content, you need to make sure that you include it in
the appropriate manifest (eg if you're adding a new math article, it will
probably end up in `badmath.json`). Using the format of the other entries
is the best way to learn the syntax.

### Building the Site

Building the site can be performed by running the `gensite.py` script,
assuming that you have all the necessary dependencies set up. If you don't,
it will probably error out somewhere along the way and hopefully tell you
what you're missing.

(Dockerfile that generates an image with all the dependencies preinstalled
coming soon)
