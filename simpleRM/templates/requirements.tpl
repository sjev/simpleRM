% reqTable=dp.requirementsTable()

# Requirements

<table >
<tr>
%for h in reqTable['header']:
    <th>{{h}}</th>
%end
</tr>
%for row in reqTable['rows']:
  <tr>
      %for i, col in enumerate(row):
      %  if i==0 :
      <td> <a href="#{{col}}">{{col}}</a></td>
     
      %  else:
      <td>{{col}}</td>
      %  end
      %end
  </tr>
%end
</table>


%for r in dp.requirements:
<a id="{{r.tag}}"></a>
### {{r.tag}} {{r.req}}
** Rationale:** {{r.rationale}} <br>
** Parent:** [{{r.parent}}](#{{r.parent}})

%end