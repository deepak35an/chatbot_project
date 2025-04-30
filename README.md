# chatbot_project

you can create virtual environment
This way your dependencies stay inside the project

      python3 -m venv venv
      source venv/bin/activate   # Mac/Linux
      venv\Scripts\activate      # Windows

step 1 
      create main folder named chatbot-projects
step 2 
      create 2 folders in chatbot-projects named static and templates
      in template create index.html
      in statics create style.css
step 3 
      in main folder(chatbot-projects) create app.py
      firstly train data by running train_model.py, will get intent_model.pkl.
      to run train_model.py, needs training_data.py
      before starting the flask server app.py needs intent_model.pkl. So, keep it file in main folder i.e chatbot-projects.
