# simpleRM

## What is it?

`simpleRM` is a barebones requirements manager tool, assisting in 
* cascading requirements decomposition
* checking requirements consistency
* documenting design during design cycle, not afterwards
* generating PDP (Product Design Documentation)

In short, this tool is designed to assist in Systems Engineering process. It provides a framework for doing [requirements decomposition](https://www.ibm.com/developerworks/community/blogs/requirementsmanagement/entry/the_practical_applications_of_traceability_part_1_what_s_really_going_on_when_you_decompose_a_requirement?lang=en)  in a structured way.


`simpleRM` is inspired by best practices used ins Systems Engineering (V-model, decompositions, validation etc), and functionality available in high-end RM systems. The main difference is that this tool aims at being as simple as possible and 'getting out of the way' enabling an architect or designer to focus on what really matters: logically decomposing high-level requirments to low-level unit requirements.



## Why simpleRM?
* because designing complex systems requires a highly structured approach
* because the process of decomposing requirements is more important than the tools used
* because architects and designers can do a better job with a good tool
* because tools should be as simple as possible, but not any simpler

## Documentation

*this project documents its own requirements decomposition and design choices, how cool is that!*

See:  https://sjev.github.io/simpleRM/


## Installation
at this moment installation is only available from source, pypi will package will be available once the project leaves alpha stage.

```
$ git clone https://github.com/sjev/simpleRM.git
$ cd simpleRM
$ python setup.py install

```


## Alternatives

* commercial requirement management packages ($$$), there are [a lot of them](http://makingofsoftware.com/resources/list-of-rm-tools)
* open-source text-based requirement managers, see [rmtoo](https://github.com/florath/rmtoo) and [doorstop](https://github.com/jacebrowning/doorstop)

## Why simpleRM again?

<img src="https://imgs.xkcd.com/comics/good_code.png"/>

...the 'question mark' is where `simpleRM` is ;-)
