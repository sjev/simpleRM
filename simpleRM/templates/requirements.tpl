<% 
# prepare functions etc
reqTable=dp.requirementsTable()

from collections import OrderedDict

icons = OrderedDict(handshake="handshake-o",
                    conflict="exclamation-triangle",
                    check="check-square-o",
                    requirement="cogs",
                    solution="lightbulb-o",
                    arrow_right="arrow-right")

def insertIcon(icon):
   return "<i class='fa fa-%s' aria-hidden='true'> </i> " % icons[icon]
end 
                   
%>

# Requirements tree

%for r in dp.requirements.values():
{{' '*4*r.level}}* {{!insertIcon('requirement')}}[{{r.tag}}](#{{r.tag}})     {{r.req}}
%end

## Legend
%for k,v in icons.items():
* <i class="fa fa-{{v}}" aria-hidden="true"> </i> : {{k}}
%end

# Dependencies
![dependencies](img/dependencies.svg)



# Detailed list
%for r in dp.requirements.values():
<a id="{{r.tag}}"></a>
** {{r.tag}} ** {{r.req}}
** Rationale:** {{r.rationale}} <br>
** Parent:** [{{r.parent}}](#{{r.parent}})

%end