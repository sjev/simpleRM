// example comment




-Requirement-
type: functional
The system **must** have a user-friendly way of writing requrements.

-Decomposition-
The easiest way of writing is just plain text. It provides the freedom of writing in users favorite editor,
and enables to focus on the process and the contents, rather than the tooling.
There are different options for text-based light-weight markup that already exist.
One of the most popular ones are

* markdown (and its flavors)
* reStructuredText

for an overview of their synthax, see [here](http://hyperpolyglot.org/lightweight-markup)

Because we need to cross-reference and tag requirements, the system also needs some kind of directive.
Being able to add commnents is a welcome feature.

The system must support requirements growing into thousands, 

--Requirement--
The system **must** use plain text input

--Reuirement--
The system **must** enable cross referencing and structuring the requirements

--Requirement---
The system **should** support comments


--Validation--
id: val01
[pandoc-flavored markdown](http://pandoc.org/MANUAL.html#pandocs-markdown) is a commonly used markup system.