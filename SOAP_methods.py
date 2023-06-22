import requests

class SOAP:

    def logOn(self, url):

        headers = {}
        body ="""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:car="http://cardlibrary2.webservices.integration.css.aamsystems.com">
   <soapenv:Header/>
   <soapenv:Body>
      <car:logon>
         <car:aUserName>1</car:aUserName>
         <car:aPassword>1</car:aPassword>
      </car:logon>
   </soapenv:Body>
</soapenv:Envelope>"""
        response = requests.post(url, data=body, headers=headers)
        # лучше отдавать статус и сессию
        if response.status == 200:
            return response.content  # поиграться и отдать сессию
        else:
            return response.status

    def get_Users_Card_Data(self, url, session):

        headers = {'content-type': 'text/xml'}
        body = f"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:car="http://cardlibrary2.webservices.integration.css.aamsystems.com">
   <soapenv:Header/>
   <soapenv:Body>
      <car:getUsersCardData>
         <car:aSession>{session}</car:aSession>
         <car:aCount>20</car:aCount>
         <car:queryId></car:queryId>
      </car:getUsersCardData>
   </soapenv:Body>
</soapenv:Envelope>"""
        response = requests.post(url, data=body, headers=headers)
        if response.status == 200:
            return response.content  # поиграться и посмотреть какие есть айдишники групп и вообще какие поля и чем заполнены на карточках
        else:
            return response.status

    def issue_card(self, url, session):
        # написать генератор - который дает имя фамилию почту и дату рождения
        # random_t_f
        # time_end   время деактивации карты в формате 2019-09-29T14:28:18.064Z
        # time_stert время активации карты в формате 2019-09-29T14:28:18.064Z
        headers = {'content-type': 'text/xml'}
        body = f"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:car="http://cardlibrary2.webservices.integration.css.aamsystems.com">
   <soapenv:Header/>
   <soapenv:Body>
      <car:issueCard>
         <car:aSession>{session}</car:aSession>
         <car:aUserId>
            <car:additionalID></car:additionalID>
            <car:primaryID></car:primaryID>
            <car:systemID></car:systemID>
         </car:aUserId>
         <car:aIssueId>
            <car:additionalID></car:additionalID>
            <car:primaryID></car:primaryID>
            <car:systemID></car:systemID>
         </car:aIssueId>
         <car:aCardId>
            <car:additionalID></car:additionalID>
            <car:primaryID></car:primaryID>
            <car:systemID></car:systemID>
         </car:aCardId>
         <car:aUserData>
            <car:birthDay>{birthDay}</car:birthDay>
            <car:category>
               <car:id>
                  <car:additionalID></car:additionalID>
                  <car:primaryID></car:primaryID>
                  <car:systemID></car:systemID>
               </car:id>
               <car:label></car:label>
            </car:category>
            <car:department>
               <car:id>
                  <car:additionalID></car:additionalID>
                  <car:primaryID></car:primaryID>
                  <car:systemID></car:systemID>
               </car:id>
               <car:label></car:label>
            </car:department>
            <car:fields>
               <!--Zero or more repetitions:-->
               <car:item>
                  <car:MName>Inactive</car:MName>
                  <car:MLabel></car:MLabel>
                  <car:MType>bool</car:MType>
                  <car:subType></car:subType>
                  <car:MValue>{random_true_false}</car:MValue>
                  <car:MName>ManagedByFIM</car:MName>
                  <car:MLabel></car:MLabel>
                  <car:MType>bool</car:MType>
                  <car:subType></car:subType>
                  <car:MValue>{random_true_false}</car:MValue>
                  <car:MName>RoomAccessByFIM</car:MName>
                  <car:MLabel></car:MLabel>
                  <car:MType>bool</car:MType>
                  <car:subType></car:subType>
                  <car:MValue>{random_true_false}</car:MValue>
               </car:item>
            </car:fields>
            <car:firstName>{firstName}</car:firstName>
            <car:id>
               <car:additionalID></car:additionalID>
               <car:primaryID></car:primaryID>
               <car:systemID></car:systemID>
            </car:id>
            <car:lastName>{lastName}</car:lastName>
            <car:middleName>{middleName}</car:middleName>
            <car:organization>
               <car:id>
                  <car:additionalID></car:additionalID>
                  <car:primaryID></car:primaryID>
                  <car:systemID></car:systemID>
               </car:id>
               <car:label></car:label>
            </car:organization>
            <car:photo></car:photo>
            <car:photoType></car:photoType>
            <car:post>
               <car:id>
                  <car:additionalID></car:additionalID>
                  <car:primaryID></car:primaryID>
                  <car:systemID></car:systemID>
               </car:id>
               <car:label></car:label>
            </car:post>
         </car:aUserData>
         <car:aCardData>
            <car:PIN></car:PIN>
            <car:accessLevels>
               <!--Zero or more repetitions:-->
               <car:item>
               <!--ID  уровня доступа забрать можно посмотрев метод  get_Users_Card_Data -->
                  <car:id> 
                     <car:additionalID>?</car:additionalID>
                     <car:primaryID>?</car:primaryID>
                     <car:systemID>?</car:systemID>
                  </car:id>
                  <car:label>?</car:label>
               </car:item>
            </car:accessLevels>
            <car:active>{random_true_false}</car:active>
            <car:endTime>{time_end}</car:endTime>
            <car:fields>
               <!--доп поля тут будет только одно - разобраться как делать если нужно несколько -->
               <car:item>
                  <car:MName>Встречающий</car:MName>
                  <car:MLabel></car:MLabel>
                  <car:MType>вообще список{list_} но лучше скоммуниздить </car:MType>
                  <car:subType>{написать подтип тоже лучше взять}</car:subType>
                  <car:MValue>{значение надо тоже передаьт желательно правильно }</car:MValue>
               </car:item>
            </car:fields>
            <car:number>{random_namber_card}</car:number>
            <car:startTime>{time_start}</car:startTime>
         </car:aCardData>
      </car:issueCard>
   </soapenv:Body>
</soapenv:Envelope>"""
        response = requests.post(url, data=body, headers=headers)
        # лучше отдавать статус и сессию
        if response.status == 200:
            return response.content  # посмотреть ответ
        else:
            return response.status

    def deactivate_card(self,url,session, ID):

        headers = {'content-type': 'text/xml'}
        body = f"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:car="http://cardlibrary2.webservices.integration.css.aamsystems.com">
   <soapenv:Header/>
   <soapenv:Body>
      <car:returnCard>
         <car:aSession>{session}</car:aSession>
         <car:aUserId>
            <car:additionalID>?</car:additionalID>
            <car:primaryID>?</car:primaryID>
            <car:systemID>?</car:systemID>
         </car:aUserId>
         <car:aUserData>
            <car:birthDay>?</car:birthDay>
            <car:category>
               <car:id>
                  <car:additionalID>?</car:additionalID>
                  <car:primaryID>?</car:primaryID>
                  <car:systemID>?</car:systemID>
               </car:id>
               <car:label>?</car:label>
            </car:category>
            <car:department>
               <car:id>
                  <car:additionalID>?</car:additionalID>
                  <car:primaryID>?</car:primaryID>
                  <car:systemID>?</car:systemID>
               </car:id>
               <car:label>?</car:label>
            </car:department>
            <car:fields>
               <!--Zero or more repetitions:-->
               <car:item>
                  <car:MName>?</car:MName>
                  <car:MLabel>?</car:MLabel>
                  <car:MType>?</car:MType>
                  <car:subType>?</car:subType>
                  <car:MValue>?</car:MValue>
               </car:item>
            </car:fields>
            <car:firstName>?</car:firstName>
            <car:id>
               <car:additionalID>?</car:additionalID>
               <car:primaryID>?</car:primaryID>
               <car:systemID>?</car:systemID>
            </car:id>
            <car:lastName>?</car:lastName>
            <car:middleName>?</car:middleName>
            <car:organization>
               <car:id>
                  <car:additionalID>?</car:additionalID>
                  <car:primaryID>?</car:primaryID>
                  <car:systemID>?</car:systemID>
               </car:id>
               <car:label>?</car:label>
            </car:organization>
            <car:photo>cid:126498889059</car:photo>
            <car:photoType>?</car:photoType>
            <car:post>
               <car:id>
                  <car:additionalID>?</car:additionalID>
                  <car:primaryID>?</car:primaryID>
                  <car:systemID>?</car:systemID>
               </car:id>
               <car:label>?</car:label>
            </car:post>
         </car:aUserData>
         <car:aIssueId>
            <car:additionalID>?</car:additionalID>
            <car:primaryID>?</car:primaryID>
            <car:systemID>?</car:systemID>
         </car:aIssueId>
         <car:aCardNumber>?</car:aCardNumber>
      </car:returnCard>
   </soapenv:Body>
</soapenv:Envelope>"""
        response = requests.post(url, data=body, headers=headers)
        if response.status == 200:
            return response.content  # поиграться и посмотреть какие есть айдишники групп и вообще какие поля и чем заполнены на карточках
        else:
            return response.status

        