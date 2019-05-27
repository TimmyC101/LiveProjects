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