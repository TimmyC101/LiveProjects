# Live-Projects

## Overview
Python Live Project - This live project took place within the Django web framework.  I was tasked with creating a graph to plot inputs from a user entry form that were then stored in a database.  This meant spending multiple days researching Django documentation and going through Django tutorials in order to understand the relationship between Django forms, modules, views, and url python files as well as Django html templates. It also required researching JavaScript chart language and syntax to properly display the visualizations.

Link to the graph can be found here: https://github.com/TimmyC101/LiveProjects/blob/master/LiveProject-Python/Habit_Graph_image.PNG

## Creating variables in views.py
First, a function had to be defined within the views.py file that would access the model object and obtain data values from that object.  These data values were represented by list variables that would later form the axes data values for the javascript chart within the html template.  These variables were passed into the html template using the return statement.

    def history_view(request):
    userEntries = Habits.objects.filter(user=request.user)
    userEntriesChron = userEntries.order_by('date')
    # create variables that (for the current user) return raw values of the fields, rather than a tuple or dictionary
    # these will then be used as data sets for the axes of the line graph contained on the html template
    entryDates = []
    entryExercise = []
    entrySleep = []
    entryMood = []
    entryEnergy = []
    entryMeditate = []
    for entry in userEntriesChron:
        entryDates.append(entry.date.strftime("%m-%d-%y")) #convert date to string
        entryExercise.append(entry.exercise)
        entrySleep.append(entry.sleep)
        entryMood.append(entry.mood)
        entryEnergy.append(entry.energy)
        # change True to 1 and False to 0 so it can be plotted by line graph on html template
        if entry.meditate == True:
            entryMeditate.append(1)
        else:
            entryMeditate.append(0)
    return render(request, 'HabitTrackerApp/habit-history.html/', {'userEntries': userEntries, 'entryDates': entryDates, 'entryExercise': entryExercise, 'entrySleep': entrySleep, 'entryMood': entryMood, 'entryEnergy': entryEnergy, 'entryMeditate': entryMeditate})

## Creating chart in html template
The variables were then pulled into the html file using the required Django syntax.  At that point, JavaScript and html were utilized in order to construct the required graph object.
I spent a lot of time perfecting the graphical display - coloration, font sizes, legend, axes labels/formatting - I even inserted a function to hide the 0 value on the axes to prevent clutter.  The "meditate" variable was an additional challenge - I converted true/false to 1/0 so that it would plot, and then converted the axis labels to yes/no to make more sense to the end user.

    {% extends 'base.html' %}
    {% load static from staticfiles %}

    {% block title %}Habit History{% endblock %}

    {% block content %}
    <script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.24.0/moment.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@2.8.0"></script>
    {% include "nav.html" %}
    <div class="center">
        <h1>Hi {{ request.user }}! Your habit history is listed below.</h1>
            <h4>If you would like to create an entry, <a href="{% url 'habit-home' %}">click here.</a></h4> <!-- Link to the habit form -->
            <br />
            <!-- create graph canvas -->
            <canvas id="habit-chart"></canvas>
            <script type="text/javascript">
            /* instantiate variables for graph, 'safe' designation prevents things like ' and " from being converting to ASCII codes */
            const entryDates = {{ entryDates|safe}};
            const entryExercise = {{ entryExercise|safe }};
            const entrySleep = {{ entrySleep|safe }};
            const entryMood = {{ entryMood|safe }};
            const entryEnergy = {{ entryEnergy|safe }};
            const entryMeditate = {{ entryMeditate|safe }};
            /* build graph */
            const habitCanvas = document.getElementById("habit-chart").getContext('2d');
            let habitChart = new Chart(habitCanvas, {
                type: "line",
                title: {
                    text: "Habit History",
                },
                data: {
                    /* x axis dataset */
                    labels: entryDates,
                    /* y axes datasets */
                    datasets: [
                        {
                            label: "Exercise (minutes)",
                            data: entryExercise,
                            /* for each dataset: set axis, apply coloration and enlarge data points */
                            yAxisID: 'A',
                            borderColor: "#389EAA",
                            pointBackgroundColor: "#389EAA",
                            pointRadius:5,
                        },
                        {
                            label: "Sleep (hours)",
                            data: entrySleep,
                            yAxisID: 'B',
                            borderColor: "#28AC60",
                            pointBackgroundColor: "#28AC60",
                            pointRadius:5,                
                        },
                        {
                            label: "Mood (Scale: 1-10)",
                            data: entryMood,
                            yAxisID: 'C',
                            borderColor: "#0000FF" ,
                            pointBackgroundColor: "#0000FF",
                            pointRadius:5,                
                        },
                        {
                            label: "Energy (Scale: 1-10)",
                            data: entryEnergy,
                            yAxisID: 'C',
                            borderColor: "#ED0414",
                            pointBackgroundColor: "#ED0414",
                            pointRadius:5,                 
                        },
                        {
                            label: "Meditate",
                            data: entryMeditate,
                            yAxisID: 'D',
                            showLine: false, /* for this dataset only show points (no line) */
                            pointBackgroundColor: "#FFFF00",
                            pointRadius:8,
                        }  

                    ]  
                },
                /* axes config and styling */
                options: {
                    title: {
                        display: false,
                        // Maintaining title formatting in the event that it is desired
                        // text: "Habit History",
                        // fontColor: "#CCC",
                        // fontStyle: "bold",
                        // fontSize: "20"
                    },
                    legend: {
                        labels: {
                            fontStyle: "bold",
                            fontColor: "#CCC"
                        }
                    },
                    scales: {
                        /* time based x axis */
                        xAxes: [
                        {
                            type: 'time',
                            time: {
                                unit: 'day'
                            },
                            ticks: {
                                fontSize: "14",
                                fontStyle: "bold",
                                fontColor: "#CCC"
                            },
                        }
                        ],
                        yAxes: [
                        {
                            /* y axis for "Exercise" dataset */
                            id: 'A',
                            type: 'linear',
                            position: 'left',
                            scaleLabel: {
                                display: true,
                                labelString: 'Exercise (minutes)',
                                fontColor: "#389EAA",
                                fontSize: "14",
                                fontStyle: "bold"
                            },
                            ticks: {
                                min: 0,
                                stepSize: 5,
                                fontColor: "#389EAA",
                                fontSize: "14",
                                fontStyle: "bold",
                                /* function to hide 0 values on axes */
                                callback: function(value, index) {
                                    if (value == 0) return "";
                                    else return value;
                                }
                            },
                            gridLines: {
                                display: false,
                            }
                        },
                        {
                            /* y axis for "Sleep" dataset */
                            id: 'B',
                            type: 'linear',
                            position: 'left',
                            scaleLabel: {
                                display: true,
                                labelString: 'Sleep (hours)',
                                fontColor: "#28AC60",
                                fontSize: "14",
                                fontStyle: "bold"
                            },
                            ticks: {
                                min: 0,
                                max: 12,
                                stepSize: 1,
                                fontColor: "#28AC60",
                                fontSize: "14",
                                fontStyle: "bold",
                                /* function to hide 0 values on axes */
                                callback: function(value, index) {
                                    if (value == 0) return "";
                                    else return value;
                                }
                            },
                            gridLines: {
                                display: false,
                            }
                        },
                        {
                            /* y axis for "Mood" & "Energy" datasets */
                            id: 'C',
                            type: 'linear',
                            position: 'right',
                            scaleLabel: {
                                display: true,
                                labelString: 'Mood/Energy (Scale: 1-10)',
                                fontColor: "#a804ed",
                                fontSize: "14",
                                fontStyle: "bold"
                            },
                            ticks: {
                                min: 0,
                                max: 10,
                                stepSize: 1,
                                fontColor: "#a804ed",
                                fontSize: "14",
                                fontStyle: "bold",
                                /* function to hide 0 values on axes */
                                callback: function(value, index) {
                                    if (value == 0) return "";
                                    else return value;
                                }
                            },
                            gridLines: {
                                display: false,
                            }
                        },
                        {
                            /* y axis for "Meditate" dataset */
                            id: 'D',
                            type: 'linear',
                            position: 'right',
                            scaleLabel: {
                                display: true,
                                labelString: 'Meditate',
                                fontColor: "#FFFF00",
                                fontSize: "14",
                                fontStyle: "bold"
                            },
                            ticks: {
                                min: 0,
                                max: 1.8, /* max set at 2 so that a "Yes" is plotted in the middle of the graph as opposed to the top */
                                fontColor: "#FFFF00",
                                fontSize: "14",
                                fontStyle: "bold",
                                /* Label axis with a "Yes" instead of a 1 for user transparency*/
                                callback: function(value, index) {
                                if (value == 1) return "Yes";
                                if (value == 0) return "No";
                                },
                            },
                            gridLines: {
                                display: false,
                            }
                        }]
                    }
                }
            })
            </script>
    </div>
    {% endblock %}

## Summary
This project was a great introduction into python and the Django web framework.  As I knew very little about the Django framework initially, the project allowed me to hone my abilities in self-sufficiency... almost all of the Django knowledge I applied on this project was self-taught/researched.  I also developed project management and team programming skills, as the project utilized Azure Devops to post user stories and manage repositories.  As a result, I became proficient in version control, git/git BASH, and python virtual environments.





