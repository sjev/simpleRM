# Welcome to simpleRM documentation


This documentation describes `requirements` , `design` and `validation` of the **simpleRM** tool




## Introduction

**simpleRM** leverages several common technologies to satisfy the requirements of a good requirements manamgement tool.

* [YAML](http://yaml.org/) - human friendly data serialization standard is used for data entry in any text editor
* git ensures that all requirements are under version control
* [MkDocs](http://www.mkdocs.org/) - produces beautiful, searchable documentation, ready for production
    
!!! note

    This documentation has been created by the **simpleRM** module itself, as an example of its usage.  
    
    
    
## Documentation workflow

Creating documentation for an engineering project typically requires these steps:

1. Enter requirements and decomposition in yaml format.
2. Use **simpleRM** to parse data, check it for consistency and create markdown docs for `requirements.md`, `solutions.md`
    and `validation.md`  
3. Edit `docs/index.md` to tie it all together
4. Build documentation with mkdocs

