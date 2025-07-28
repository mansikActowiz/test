

'''my working code starts'''


from django.shortcuts import render, HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import io



def feasibility_form_view(request):
    if request.method == 'POST':
        domain_name= request.POST.get('domain_name')
        domain_link= request.POST.get('domain_link')
        input_methods=request.POST.get('input_methods')
        # location=request.POST.get('location')

        location = request.POST.get('location')  # 'region', 'zipcode', or 'store'
        location_value = ""

        if location == "Region":
            country = request.POST.get('country', '')
            region = request.POST.get('region_name', '')
            location_value = f"Region : {region} Country - {country}"
        elif location == 'Zipcode':
            zipcode = request.POST.get('zipcode', '')
            location_value = f"Zipcode - {zipcode}"
        elif location == 'Store number/Store name':
            store = request.POST.get('store_name', '')
            location_value = f"Store - {store}"

        context = {
            # other fields...
            'location': location_value,
            # other fields...
        }

        language=request.POST.get('language')
        frequency= request.POST.get('frequency')
        data_volume= request.POST.get('data_volume')
        output_format= request.POST.get('output_format')
        # data_fields= request.POST.get('data_fields')

        # Extract all dynamic fields
        field_data = []
        for key in request.POST.keys():
            if key.startswith('field_name_'):
                index = key.split('_')[-1]
                name = request.POST.get(f'field_name_{index}')
                desc = request.POST.get(f'field_desc_{index}')
                datatype = request.POST.get(f'datatype_{index}')
                mandatory = request.POST.get(f'mandatory_{index}')
                if name or desc:
                    field_data.append({
                        'name': name,
                        'desc': desc,
                        'datatype': datatype,
                        'mandatory': mandatory
                    })

        delivery_format= request.POST.get('delivery_format')
        platform_of_delivery= request.POST.get('platform_of_delivery')
        notes=request.POST.get('notes')


        context = {
            'domain_name': domain_name,
            'domain_link': domain_link,
            'input_methods': input_methods,
            # 'location': location,
            'location': location_value,
            'language': language,
            'frequency': frequency,
            'data_volume': data_volume,
            'output_format': output_format,
            'data_fields': field_data,
            'delivery_format':delivery_format,
            'platform_of_delivery': platform_of_delivery,
            'notes':notes,
        }

        request.session['form_data'] = context

        return render(request, 'form_result.html', context)

    return render(request, 'form.html')






def generate_pdf(request):
    context = request.session.get('form_data')
    if not context:
        return HttpResponse("No data found to generate PDF.")

    template = get_template('form_result_pdf.html')
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="feasibility_form.pdf"'

    pisa_status = pisa.CreatePDF(
        io.BytesIO(html.encode('utf-8')),
        dest=response,
        encoding='utf-8'
    )

    # Optional: clear session data
    del request.session['form_data']

    if pisa_status.err:
        return HttpResponse("Error generating PDF")
    return response



def index(request):
    context = {
        'variable': 'this is actowiz'
    }
    return render(request, 'index.html', context)


def about(request):
    return HttpResponse('this is about page')

def service(request):
    return render(request, 'service.html')
    # return HttpResponse('this is service page')

'''my working code ends'''