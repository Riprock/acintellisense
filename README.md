# Assetto Intellisense
Library containing fuction stubs to help with Assetto Corsa mod development when using an IDE

Helps internal intellisense to know function calls with types.

This recreates the `ac` module with currently known stubs



Python Pacakage: 
## Installation to develop AC mod

You will need to install the package in your environment:
```shell
pip install assetto-intellisense
```

Now if your PyCharm project is accessible to this package,
after `import ac`, you should be able to use autocomplete.

Now you can check your IDE, autocomplete shall work.


## Contribution
Please submit issues/pull requests if there is something missing, documentation inaccuracy, or a revision
I am trying to keep this as up to date as possible to help in mod development

Any and all work on this is appreciated! 

For a list of functions missing documetation: [Missing Functions](missing_functions.md)

## References
#### Thank yous/Credits:
[rikby/ac-stubs](https://github.com/rikby/ac-stubs) - These guys did a bunch of the heavy lifting by getting all the function stubs. I just modified it and documented it. The only reason why this repository exists is that its been over a year since that repository was updated and I saw that there was still room to imporve on it and with the pull request I made remaing open, I decided to create this to continue its inital purpose by helping modders when it comes to IDE intellisense

#### Source documents:
- https://docs.google.com/document/d/13trBp6K1TjWbToUQs_nfFsB291-zVJzRZCNaTYt4Dzc/pub
- https://assettocorsamods.net/attachments/inofficial_acpythondoc_v2-pdf.7415/
- https://www.assettocorsa.net/forum/index.php?threads/python-doc-update-25-05-2017.517/

#### Initial forum threads:
- https://assettocorsamods.net/threads/doc-python-doc.59
- https://assettocorsamods.net/threads/is-there-a-way-to-load-ac-library-to-have-autocomplete-in-an-ide-e-g-pycharm.3088/
