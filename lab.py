            db.collection(u'epa-method-9-forms').document(u'record-1').child('section_a').child('company_name').push(company_name) 
            db.collection(u'epa-method-9-forms').document(u'record-1').child('section_a').child('street_address').push(street_address)
            db.collection(u'epa-method-9-forms').document(u'record-1').child('section_a').child('city').push(city)
            db.collection(u'epa-method-9-forms').document(u'record-1').child('section_a').child('state').push(state)            
            db.collection(u'epa-method-9-forms').document(u'record-1').child('section_a').child('zip').push(zip_code)
            db.collection(u'epa-method-9-forms').document(u'record-1').child('section_a').child('phone_key_contact').push(phone_key_contact)
            db.collection(u'epa-method-9-forms').document(u'record-1').child('section_a').child('source_id_number').push(source_id_number)


                        print(u'{}'.format(company_name))
            print(u'{}'.format(street_address))
            print(u'{}'.format(city))
            print(u'{}'.format(state))
            print(u'{}'.format(zip_code))
            print(u'{}'.format(phone_key_contact))
            print(u'{}'.format(source_id_number))  