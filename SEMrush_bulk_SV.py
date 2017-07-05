import requests
 
# Sorgente delle keyword da analizzare  
queries_file = "query.txt"

# API_KEY di SEMRush eventualmente da richiedere

API_key = "<YOUR-API-KEY>"
 
# Ciclo per ogni keyword del file
queries = [line.rstrip('\n') for line in open(queries_file)]
  

# File di testo aperto in scrittura per salvare il result dell'interrogazione di SEMRush API

the_file = open("SEMRush.txt", "w")

# Header del file di response 
the_file.write("Keyword,Search Volume,CPC,Competition,No. of Results \n")


# Loop nelle keyword da interrogare nei sistemi di SEMRush 
for query in queries:
    # Lista per il result set
    the_list = []
    # url della request verso SEMRush su database IT - per keywork italiane
    url = "http://api.semrush.com/?type=phrase_this&key=" + API_key + "&export_columns=Ph,Nq,Cp,Co,Nr&phrase=" + query + "&database=it"
    print url # stampiamo la url per controllo di correttazza
    result = (requests.get(url).text).split(';')
    keyword = the_list.append(query)
    # Add SEMRush data to the list

    try:
        search_vol = the_list.append(result[5]) # Search Volume
        cpc = the_list.append(result[6]) # CPC 
        comp = the_list.append(result[7]) # COMP
        no_results = the_list.append(result[8]) # No result
 
    # Se la richiesta verso SEMRush non funziona oppure non ha "search volume" inseriamo ERROR
    except:
        the_list.append("NO SEARCH VOLUME")
    the_list.append("\n")
    
    # Scriviamo sul file di output il risultato dell'interrogazione separato da ,

    the_file.write(",".join(the_list))
    
    # Stampiamo a video i dati dell'interrogazione andata a buon fine su SEMRush 
    print the_list
  
# Chisuura dello stream verso il file.
the_file.close
