import requests
from bs4 import BeautifulSoup
import json

"""
Utility functions to get the *freguesia* for each postal code.
"""

def get_from_duminio(postal_code):
    try:
        response = requests.get(f'https://api.duminio.com/ptcp/ptapi5fac723898cd62.64119931/{postal_code}', timeout=0.5) # Using API version 1 (only returns 1 element from postal code)
    except Exception as e:
        print(f'Something went wrong. Response timed out.')
        return {'Error': e}

    if response.status_code == 200:
        try:
            response_string = response.content.decode('utf-8')
            #print(response_string)

            response_string = response_string.replace('<i>Desconhecido</i>', '')
            response_string = response_string.replace(': ,', ': "",')
            response_string = response_string.replace(': }', ': ""}')

            return json.loads(response_string)
            #return response.json()
        except Exception as e:
            return {'Error': e}
    else:
        print(f'Something went wrong. Response status code: {response.status_code}.')
        return {'Error': response.status_code}

def get_from_cod_postal(distrito, concelho, localidade, cod_postal):
    payload={'rua': '', 'local': localidade}
    try:
        response = requests.get('https://www.codigo-postal.pt/', params=payload, timeout=1)
    except Exception as e:
        #print(f'Something went wrong. Response timed out.')
        return {'Error': e}

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        N_pgs = 1
        for tag in soup.find_all('div'):
            try:
                if 'pagination-container' in tag['class']:
                    for t in tag.find_all('div'):
                        N_pgs = int(t.string.split(' ')[-1])
                        #print(N_pgs)
            except KeyError:
                ...

        for pg in range(1, N_pgs+1):
            try:
                payload['p'] = pg
                response = requests.get('https://www.codigo-postal.pt/', params=payload, timeout=1)
                #print(response.url)
            except Exception as e:
                #print(f'Something went wrong. Response timed out.')
                return {'Error': e}

            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                for tag in soup.find_all('div'):
                    try:
                        if tag['class'][0] == 'places':
                            for tag_places in tag.find_all('p'):
                                try:
                                    if not tag_places.attrs or tag_places['class'][0] == 'odd':
                                        cod_postal_found = False
                                        for tag_local in tag_places.find_all('span'):
                                            try:
                                                if not cod_postal_found and tag_local.string.replace('-', '') == str(cod_postal):
                                                    cod_postal_found = True
                                                    next

                                                if cod_postal_found:
                                                    string_split = tag_local.string.split(',')
                                                    if len(string_split) > 1:
                                                        dcfre = {}

                                                        dcfre['Freguesia'] = string_split[0]
                                                        
                                                        if len(string_split) == 3:
                                                            dcfre['Concelho'] = string_split[1]
                                                            dcfre['Distrito'] = string_split[2]
                                                        elif len(string_split) == 2:
                                                            dcfre['Concelho'] = string_split[1]
                                                            dcfre['Distrito'] = string_split[1]

                                                        #if dcfre['Distrito'].replace(' ', '') == 'Aveiro':
                                                            #print(dcfre, pg)

                                                        if dcfre['Distrito'].replace(' ', '') == distrito.replace(' ', '') and \
                                                        dcfre['Concelho'].replace(' ', '') == concelho.replace(' ', ''):
                                                            return dcfre
                                            except:
                                                ...                
                                except KeyError:
                                    ...
                    except KeyError:
                        ...
    return {}

if __name__ == '__main__':
    postal_code = '2590432'
    #print(get_from_duminio(postal_code))
    #print(get_from_cod_postal('Perre'))