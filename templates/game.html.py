<!doctype html>
<title>Sudoku</title>
<link rel="stylesheet" type="text/css" href="{{url_for('static',filename='style.css')}}">
<script type="text/javascript" src="{{url_for('static',filename='jquery-1.11.3.min.js')}}"></script>
<script type="text/javascript" src="{{url_for('static',filename='style_helper.js')}}"></script>

<div class='header-wrap'>
    <h1 class='title'>sudoku</h1>
    <ul class='levels'>
        {% for item in range(1,6) %}
            <li class='level'>{{ item }}</li>
        {% endfor %}
    </ul>
</div>
<br>
<div class='control-wrap'>
    <table class='puzzle'>
        {% for row in puzzle %}
            {% set i = loop.index %}
            <tr>
                {% for elem in row %}
                    {% set j = loop.index %}
                    <td>
                        {% if ((i<=3) and (j<=6) and (j>3)) %}
                        <div id='cell{{i}}{{j}}' class='dark'>
                            {% if elem %}
                                {{elem}}
                            {% endif %}
                        </div>
                        {% elif ((i>6) and (j<=6) and (j>3)) %}
                        <div id='cell{{i}}{{j}}' class='dark'>
                            {% if elem %}
                                {{elem}}
                            {% endif %}
                        </div>
                        {% elif ((j<=3) and (i<=6) and (i>3)) %}
                        <div id='cell{{i}}{{j}}' class='dark'>
                            {% if elem %}
                                {{elem}}
                            {% endif %}
                        </div>
                        {% elif ((j>6) and (i<=6) and (i>3)) %}
                        <div id='cell{{i}}{{j}}' class='dark'>
                            {% if elem %}
                                {{elem}}
                            {% endif %}
                        </div>
                        {% else %}
                        <div id='cell{{i}}{{j}}' class='light'>
                            {% if elem %}
                                {{elem}}
                            {% endif %}
                        </div>
                        {% endif %}
                    </td>
                {% endfor %}
            </tr>
        {% endfor %}
    </table>

    <ul class='selector'>
        {% for item in range(1,10) %}
            <li class='fill'>{{ item }}</li>
        {% endfor %}
    </ul>
</div>

<!-- <div class='bottom-wrap'>
<div id='share' class='button'>share</div>
</div> -->