from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os.path


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get the form data
    full_name = request.form.get('fullName')
    email = request.form.get('email')
    contact = request.form.get('contact')
    linkedin = request.form.get('linkedin')
    city = request.form.get('city')
    cayear = request.form.get('cayear')
    current_company = request.form.get('currentCompany')
    turnover = request.form.get('turnover')
    origin = request.form.get('orgin')
    B2BorB2C = request.form.get('B2BorB2C')
    ListingStatus = request.form.get('ListingStatus')
    pestatus = request.form.get('pestatus')
    sector = request.form.get('sector')
    currency = request.form.get('currency')
    fixedctc = request.form.get('fixedctc')
    variablectc = request.form.get('variablectc')
    esops = request.form.get('esops')
    ltbenefits = request.form.get('ltbenefits')
    cashbenefits = request.form.get('cashbenefits')
    otherbenefits = request.form.get('otherbenefits')
    total_annual = request.form.get('totalAnnual')

    data = {
        'Full Name': [full_name],
        'Contact': [contact],
        'Email': [email],
        'LinkedIn': [linkedin],
        'Current City': [city],
        'CA Year': [cayear],
        'Current Company': [current_company],
        'Turnover': [turnover],
        'Origin': [origin],
        'B2BorB2C': [B2BorB2C],
        'ListingStatus': [ListingStatus],
        'PE status': [pestatus],
        'Sector': [sector],
        'Currency': [currency],
        'Fixed CTC': [fixedctc],
        'Variable CTC': [variablectc],
        'ESOPS': [esops],
        'Long Term Benefits': [ltbenefits],
        'Cash Benefits': [cashbenefits],
        'Other Benefits': [otherbenefits],
        'Total Annual': [total_annual]
    }

    # Check if the Excel file already exists
    if os.path.isfile('form_data.xlsx'):
        # Load the existing data from the file
        existing_data = pd.read_excel('form_data.xlsx')
        # Concatenate the existing data with the new form data
        updated_data = pd.concat([existing_data, pd.DataFrame(data)], ignore_index=True)
        # Save the updated data to the Excel file
        updated_data.to_excel('form_data.xlsx', index=True)
    else:
        # Create a new DataFrame with the form data
        df = pd.DataFrame(data)
        # Save the DataFrame to an Excel file
        df.to_excel('form_data.xlsx', index=False)

    # Redirect to the display page with form data as query parameters
    return redirect(url_for('display', fullName=full_name, contact=contact, email=email, linkedin=linkedin,
                            city=city, cayear=cayear,currentCompany=current_company, 
                            turnover= turnover, origin=origin, B2BorB2C=B2BorB2C,
                            ListingStatus=ListingStatus, pestatus=pestatus, sector=sector,currency=currency, 
                            fixedctc=float(fixedctc), variablectc=float(variablectc), esops=float(esops), ltbenefits=float(ltbenefits), 
                            cashbenefits=float(cashbenefits),otherbenefits=float(otherbenefits),totalAnnual=float(total_annual)))

@app.route('/display')
def display():
    return render_template('display.html')

if __name__ == '__main__':
    app.run(debug=True)
