def AddClient(newclientip):
    editline = 20
    with open('/templates/index.html', '+', encoding='utf-8') as parsedfile:
        readdata = parsedfile.readlines()
        
        readdata[editline] = "                    <option>\n"
        
        parsedfile.writelines()
        
    
    