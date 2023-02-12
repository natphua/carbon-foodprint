from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates', static_folder='static')

# data for carbon footprint of foods 
foodName = ['Wheat & Rye (Bread)','Maize (Meal)','Barley (Beer)', 'Oatmeal','Rice','Potatoes','Cassava', 'Cane Sugar','Beet Sugar','Other Pulses','Peas','Nuts','Groundnuts','Soymilk',
'Tofu','Soybean Oil','Palm Oil','Sunflower Oil','Rapeseed Oil','Olive Oil','Tomatoes','Onions & Leeks','Root Vegetables','Brassicas','Other Vegetables','Citrus Fruit','Bananas','Apples','Berries & Grapes','Wine','Other Fruit','Coffee','Dark Chocolate','Beef','Bovine Meat (dairy herd)','Lamb & Mutton','Pig Meat','Poultry','Milk','Cheese','Eggs','Fish (farmed)','Crustaceans (farmed)','Cereals & Oilcrops Misc.','Oils Misc.','Sweeteners & Honey','Stimulants & Spices Misc.','Animal Fats','Buffalo','Butter, Cream & Ghee','Fish & Crustaceans (capture)','Aquatic Plants']
ghg = [0.1, 0.3, 0.0, 0.0, 0.0, 0.0, 0.6, 1.2, 0.0, 0.0, 0.0,-2.1,0.4,0.2, 1.0, 3.1,3.1,0.1,0.2, -0.4, 0.4, 0.0, 0.0, 0.0,0.0,-0.1,0.0,0.0,0.0,-0.1,0.1,3.7,14.3,16.3,0.9, 0.5,1.5,2.5,0.5,4.5,0.7,0.5,0.2,0.2,2.0,0.0,6.0,2.0,9.6,0.5, 0.0,0.0]
# amount of kilograms emitted per one kilogram of product produced
df = {"None": 0.0}
for i in range(len(ghg)):
  df[foodName[i]] = ghg[i]

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/select")
def food_select(): 
  return render_template("food.html")

@app.route("/result", methods=['GET','POST'])
def getvalue():
  protein = request.form['proteins']
  protein2 = request.form['proteins2']
  fruit = request.form['fruits']
  drink = request.form['drink']
  carbs = request.form['carbs']
  vegetable = request.form['vegetable']
  extra = request.form['condiments']
  result = df[protein] + df[protein2] + df[fruit] + df[carbs] + df[vegetable] + df[drink] + df[extra]
  result = df[protein]
  return render_template("result.html", result=result)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True, port=80)
