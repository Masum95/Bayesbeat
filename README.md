Running the systems locally
================================
Execute the `run.sh` file

About Heroku Integration
===============================
[Heroku app link](https://buetian-db.herokuapp.com/)  

In order to push the server to heroku, use  
`git subtree push --prefix server heroku master`

Dummy Link
===========
Make a request to `/dummy/` to get the following response: 
```
{  
    "data": "Hello world!",
    "status": "OK"
}
```

API documentation
==================
You will need access to client id and client secret to be able to make api
requests. Read [this](https://github.com/RealmTeam/django-rest-framework-social-oauth2#setting-up-a-new-application)
to know how to get this.

Creating new user with Facebook
--------------------------------
First get your access token and user-id from the front-end. This should look like this.
```json
{
  "accessToken": "<acccess_token>",
  "userID": "<uid>",
  "expiresIn": 5845,
  "signedRequest": "Un3cxjvF_2MTioaNX8e8V3BtN3GJEsa3-E3VwY3oVYA.eyJ1c2VyX2lkIjoiMTEwOTUzNzE1OTQwNjU5NSIsImNvZGUiOiJBUURNUi1CWmQxQzBzdzFGeHhIUXBXRVFFaS1TOUZHOGlxRUhQTWMxcEg4S0d2VzdHdENOZl80enBDaDRmM2tNRVlTOUlWWnhLeFYteHEyTm50eHpOWnpWX0U2dlE0Y1VLVXd1NkVHUmpJZ1hOUzczV0VMaWYtNEN1TGxUUzZpNktxWjZxVUhjQVJ1Y1BrY2lsMzNWVjZyVU1hVDByTnRZVXljdGFDN3BKcTJ4bHNrWEl0X0x2aFE1amUtdWZIU2ZuaWFmSTA5bWhXRWQ4Rm1tbXhfcVR0VHY2LUstYmZzYWZnN3YtRUZieFZZXzlWTTFWQnRuRnktWnFXZU13Wk1SR1RHTWpheXlweWprRlh4aG9FeDA3RGU4XzNrTjRKcTdiSm8xZkZqT3N4YUhHR3RGNjlud0x1bjkzaVVwdHZOdVllZGx6bkloS2pvZ3pXZGNoS0t1RFZzbmdBc3hhcF9wc0J2WnAxaUpYSTF3YWciLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTU5MDc2NTc1NX0",
  "graphDomain": "facebook",
  "data_access_expiration_time": 1598541755
}
```  
Take the access token and make the following request
```bash
curl -X POST -d "grant_type=convert_token&client_id=<client_id>&client_secret=<client_secret>&backend=<backend>&token=<backend_token>" http://localhost:8000/auth/convert-token
```
You will get a response like the following in return
```json
{
  "access_token": "xEVdPbgomEb1MBn8EaMVHeles3ATwi",
  "expires_in": 36000,
  "token_type": "Bearer",
  "scope":"read write",
  "refresh_token":"f4i7KV1Xv8ngYTSzCgfgPInHjcH4Hd"
}
```
Hurrah! You got your access token and refresh token!

Refresh your token
------------------
Make the following request
```bash
curl -X POST -d "grant_type=refresh_token&client_id=<client_id>&client_secret=<client_secret>&refresh_token=<your_refresh_token>" http://localhost:8000/auth/token
```
You should get a response like the one you got earlier

Revoke a single token
---------------------
```bash
curl -X POST -d "client_id=<client_id>&client_secret=<client_secret>&token=<your_token>" http://localhost:8000/auth/revoke-token
```

Revoke all tokens for a user
----------------------------
```bash
curl -H "Authorization: Bearer <token>" -X POST -d "client_id=<client_id>" http://localhost:8000/auth/invalidate-sessions
```

Authorizing your request
------------------------
In order to get access to protected resources, tell us who you are by
adding the access token you got in the authorization header. The token is
bearer type. So, the header will look like this `Authorization: Bearer <access_token>`