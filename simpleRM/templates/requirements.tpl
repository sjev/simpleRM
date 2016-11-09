% reqTable=dp.requirementsTable()

# Requirements

%for r in dp.requirements.values():
{{' '*4*r.level}}* [{{r.tag}}](#{{r.tag}})     {{r.req}}
%end





%for r in dp.requirements.values():
<a id="{{r.tag}}"></a>
### {{r.tag}} {{r.req}}
** Rationale:** {{r.rationale}} <br>
** Parent:** [{{r.parent}}](#{{r.parent}})

%end