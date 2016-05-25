# DesignSafe Community Forums

## Setup

1. Create an Agave Client with callback url set to `<hostname:port>/auth/agave/callback/`
   For example, for local Django runserver, using the Agave CLI:
   
   ```
   clients-create -N designsafe-forums -C http://127.0.0.1:8000/auth/agave/callback/
   ```
   
2. Copy `env.sh.example` to `env.sh`. Add Agave client key and secret from step 1 as
   appropriate.

3. Source the environment files and start the development server:

   ```
   source env.sh && python dsforums/manage.py runserver
   ```

4. Open http://127.0.0.1:8000 in your browser and profit!


