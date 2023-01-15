from django.shortcuts import render, redirect
from django.views import View
import sys
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import numpy as np
from random import randint, choice
import math
import requests
import json

class Dashboard(View):
    template_name:str = 'home.html'

    def get(self, request):

        return render(request, self.template_name)
class sipcalculator(View):

    template_name: str = 'sipcalculator.html'
    
    def get(self, request):
        print("runningggg")
      
        return render(request, self.template_name, locals())
    
    def post(self, request):
        
        monthly_amount = int(request.POST.get("monthly_amount"))
        rate = int(request.POST.get("rate"))
        years = int(request.POST.get("year"))
        annual_inc = int(request.POST.get("annual_increase"))
        monthly_rate = rate/12/100
        M = years * 12
        amount_invested = monthly_amount * M
        increament_amount = int(monthly_amount / annual_inc)
        monthly_inc = monthly_amount
        with_increment = 0
        total_rest_amount_invested = 0
        total_gain = 0
        sip_one_ammount = 0
        fv_for_oneyear = 0
        monthly_rate = rate/12/100
        amount_invested_with_inc = 0
        one_year_investment = 0
        for i in range(1,years+1):
            if i == 1:
                fv_for_oneyear = monthly_amount * ((((1 + monthly_rate)**(12))-1) * (1 + monthly_rate))/monthly_rate
                print(fv_for_oneyear,"fv_for_oneyearfv_for_oneyearfv_for_oneyear")
                one_year_investment = monthly_amount * 12
                print(one_year_investment,"one_year_investmentone_year_investmentone_year_investmentone_year_investment")

            else:
                monthly_inc = monthly_inc + increament_amount
                fv_for_restyear = monthly_inc * ((((1 + monthly_rate)**(12))-1) * (1 + monthly_rate))/monthly_rate
                amount_invested_with_inc = amount_invested_with_inc + (monthly_inc * 12)
                total_gain = total_gain + fv_for_restyear

        expected_amount = int(fv_for_oneyear + total_gain)
        amount_invested = amount_invested_with_inc + one_year_investment
        wealth_gain = round(expected_amount-amount_invested)
        return render(request, self.template_name, locals())

class MilealgeCalculator(View):
    
    template_name:str = 'mileage_calculator.html'

    def get(self, request):
        return render(request, self.template_name, locals())
    def post(self, request):
        km = int(request.POST.get("km"))
        petrol_mileage = int(request.POST.get("petrol_mileage"))
        diesel_mileage = int(request.POST.get("diesel_mileage"))
        cng_mileage = int(request.POST.get("diesel_mileage"))
        
        petrol_price = float(request.POST.get("petrol_price"))
        diesel_price = float(request.POST.get("diesel_price"))
        cng_price = float(request.POST.get("cng_price"))

        daily_petrol_cost = round(km / petrol_mileage * petrol_price)
        daily_diesel_cost = round(km / diesel_mileage * diesel_price)
        daily_cng_cost = round(km / cng_mileage * cng_price)
        
        monthly_petrol_cost = daily_petrol_cost  * 30
        monthly_diesel_cost = daily_diesel_cost * 30
        monthly_cng_cost = daily_cng_cost * 30

        Yearly_petrol_cost = monthly_petrol_cost * 12
        Yearly_diesel_cost = monthly_diesel_cost * 12
        Yearly_cng_cost = monthly_cng_cost * 12

        return render(request, self.template_name, locals())

class PositionSizeCalculator(View):
    template_name: str = 'position_size.html'

    def get(self, request):
        return render(request, self.template_name, locals())
    def post(self, request):
        capital = request.POST.get("capital")
        per_risk_capital= request.POST.get("per_risk_capital")
        buy_price= request.POST.get("buy_price")
        stop_loss= request.POST.get("stop_loss")
        risk = (float(per_risk_capital) / 100) * int(capital)
        risk_percentage = int(((int(buy_price) - int(stop_loss)) / int(buy_price)) * 100)
        position_size = int(risk / (int(buy_price)-int(stop_loss)))
        cash = position_size * int(buy_price)

        return render(request, self.template_name, locals())


class CurrencyConverter(View):
    template_name: str = 'currency.html'

    def get(self, request):
        return render(request, self.template_name, locals())
    def post(self, request):
        
        currency_from = request.POST.get("currency_from")
        currency_to = request.POST.get("currency_to")
        amount = request.POST.get("amount")
        url = "https://api.apilayer.com/currency_data/convert?to={}&from={}&amount={}".format(currency_to,currency_from, int(amount))

        payload = {}
        headers= {
        "apikey": "pnoDny68WL0NDWpXmtKZoJU8bunsLrGL"
        }

        response = requests.request("GET", url, headers=headers, data = payload)

        status_code = response.status_code
        result = response.text
        output = json.loads(result)
        converted = output["result"]

        return render(request, self.template_name, locals())