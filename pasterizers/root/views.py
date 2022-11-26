from django.shortcuts import render
from .forms import ParameterForm
from django.db import connection
import matplotlib.pyplot as plt


plt.switch_backend('agg')


def index(request):
    return render(request, 'root/index.html')


def plot_figure(form, table):
    cursor = connection.cursor()
    params_list = ['temp_past', 'press_past', 'temp_cool', 'pu', 'o2', 'flow']
    day = form.cleaned_data.get('day')
    params = form.cleaned_data.get('parameters')
    hour_from = form.cleaned_data.get('hour_from')
    hour_to = form.cleaned_data.get('hour_to')
    cursor.execute(
        f"SELECT time FROM {table} WHERE date = '{day}'" +
        f" AND time BETWEEN '{hour_from}:00:00' AND '{hour_to}:00:00';")
    timeline = cursor.fetchall()
    timeline_format = []
    for i in timeline:
        timeline_format.append(str(*i))
    if params_list[0] in params:
        cursor.execute(
            f"SELECT {params_list[0]} FROM {table} WHERE date = '{day}'" +
            f" AND time BETWEEN '{hour_from}:00:00' AND '{hour_to}:00:00';")
        temp_past = cursor.fetchall()
        plt.plot(timeline_format, temp_past)
    if params_list[1] in params:
        cursor.execute(
            f"SELECT {params_list[1]} FROM {table} WHERE date = '{day}'" +
            f" AND time BETWEEN '{hour_from}:00:00' AND '{hour_to}:00:00';")
        press_past = cursor.fetchall()
        plt.plot(timeline_format, press_past)
    if params_list[2] in params:
        cursor.execute(
            f"SELECT {params_list[2]} FROM {table} WHERE date = '{day}'" +
            f" AND time BETWEEN '{hour_from}:00:00' AND '{hour_to}:00:00';")
        temp_cool = cursor.fetchall()
        plt.plot(timeline_format, temp_cool)    
    if params_list[3] in params:
        cursor.execute(
            f"SELECT {params_list[3]} FROM {table} WHERE date = '{day}'" +
            f" AND time BETWEEN '{hour_from}:00:00' AND '{hour_to}:00:00';")
        pu = cursor.fetchall()
        plt.plot(timeline_format, pu) 
    if params_list[4] in params:
        cursor.execute(
            f"SELECT {params_list[4]} FROM {table} WHERE date = '{day}'" +
            f" AND time BETWEEN '{hour_from}:00:00' AND '{hour_to}:00:00';")
        o2 = cursor.fetchall()
        plt.plot(timeline_format, o2)
    if params_list[5] in params:
        cursor.execute(
            f"SELECT {params_list[5]} FROM {table} WHERE date = '{day}'" +
            f" AND time BETWEEN '{hour_from}:00:00' AND '{hour_to}:00:00';")
        flow = cursor.fetchall()
        plt.plot(timeline_format, flow)
    plt.savefig('static/figures/figure.png')
    plt.clf()
    cursor.close()    


def line_view(request, page, table):
    submitbutton = request.POST.get('submit')
    form = ParameterForm(request.POST or None)
    if form.is_valid():
        plot_figure(form, table)
        context = {
            'form': form,
            'submitbutton': submitbutton,
        }
        return render(request, page, context)
    return render(request, page, {'form': form})    


def pet4(request):
    return line_view(request, 'root/PET-4.html', 'pet4')


def glass6(request):
    return line_view(request, 'root/GLASS-6.html', 'glass6')      


def can1(request):
    return line_view(request, 'root/CAN-1.html', 'can1')


def pet2(request):
    return line_view(request, 'root/PET-2.html', 'pet2')


def petkeg(request):
    return line_view(request, 'root/PET-KEG.html', 'petkeg')


def keg(request):
    return line_view(request, 'root/KEG.html', 'keg')


def help(request):
    return render(request, 'root/help.html')


def contacts(request):
    return render(request, 'root/contacts.html')


def review(request):
    return render(request, 'root/review.html')
