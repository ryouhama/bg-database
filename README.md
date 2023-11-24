# bg-database
...


# Setup

## Python
This project uses [rye](https://rye-up.com/) for package management. The setup for rye is prepared in the [Makefile](./Makefile?plan=1#L1).

### 1. Install Rye
Please install Rye locally following the Rye installation guide.  
[Install Guide](https://rye-up.com/guide/installation/)

### 2. Create .venv
To create a local `.venv`, execute the following command:
```shell
make py.setup
```

If you need to recreate the local .venv, please execute the following command:
```shell
make py.update
```


## [Supabase CLI](https://supabase.com/docs/reference/cli/supabase-init)
All operations in Supabase are managed by the [Makefile](./Makefile?plan=1#L9). You can execute any Supabase operation using make `supa.xxx`.

### 1. Install CLI and Login
Use [brew](https://brew.sh/) to install the Supabase CLI. Then, log in to Supabase with the following commands:
```shell
make supa.setup
make supa.login
```

### 2. Start
To start Supabase, use the following command:
```shell
make supa.up
```
Then, access your local project at
[localhost](http://localhost:54323/project/default)

### 3. Stop
Use the following command to stop the local Supabase without creating any backup files:
```shell
make supa.down
```

# Development

## Start dev server
To start the development server, run the following command:
```shell
rye run uvicorn main:app --reload
```
Then, access the Swagger documentation at [localhost](http://localhost:8000/docs)

