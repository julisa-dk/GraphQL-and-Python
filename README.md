1. Create virtual env. run d commend python -m venv ./env
2. Activate env (for Windows)   ./env/Scripts/Activate.ps1   (deactivate)
3. pip install ariadne
4. pip freeze
5. pip freeze > requirements.txt
6. Install dependencies pip install -r requirements.txt

7. Async. web server for python   pip install 'uvicorn[standard]'
8. Run the server(note: put variable grapg_app from file server.py)  uvicorn server:graph_app --reload
9. Step 1: set message into the message cube and send it to the source
10. Create server.py 
11. Gonna need from ariadne - sql, make_schema, subscription and mutation for send the message 
12. Gonna need FastAPI
13. Set up "type definition" - type_def
14. Define the mutation 
mutation = MutationType()
mutation.set_field("setMessage", resolve_set_message)
  or
@mutation.field("setMessage")

15. Make the schema with type_def and also mutation
16. Need to import GraphQL from ariadne
17. Add web socket
18. Install uvicorn : pip install ´uvicorn[standard]´
19. Update requirements.txt :  pip freeze > requirements.txt  
20. Run the server : unicorn server:app --reload
21. Open localhost:8000
22. Check the connection: add the query
mutation{
  setMessage(text: "Hi Julia")
}

23. Add connection with broadcaster for the send message

24. Step 2: Connect to the message cube with broadcaster
25. Create async function for set message (publish in ariadne)
26. Create subscription for listening message cube when it get new message (use chanel)
