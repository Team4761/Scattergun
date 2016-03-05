{% comment %}
dataname should be some unique identifier for the graph
datasets should be an array with each data entry looking like
{
    name
    xy: {[x,y]}
}
{% endcomment %}
var data = {
    series:[
    {% for data in datasets %}
    {
        name: {{data.name}},
        data: [{% for xy in data.xy %}
            {x: {{ xy.x }}, y: {{ xy.y }}},
            {% endfor %}
        ]
    },
    {% endfor %}
    ] 
};
    
var settings = {
    lineSmooth: false,
    axisX: {
    type: Chartist.AutoScaleAxis,
    onlyInteger: true,}
};
    
new Chartist.Line('#{{dataname}}', data, settings);
