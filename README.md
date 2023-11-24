# bg-database

Describe your project here.


## Setup

### [Supabase CLI](https://supabase.com/docs/reference/cli/supabase-init)
All operations in Supabase are managed by the [Makefile](./Makefile).  
Everything you want to do in Supabase can be executed from `make supa.xxx`.

### 1. Install CLI and Login
Use [brew](https://brew.sh/) to install the supabase CLI.  
Then, log in to supabase.
```shell
make supa.setup
make supa.login
```

### 2. Start
```shell
make supa.up
```
Access to [local](http://localhost:54323/project/default)

### 3. Stop
This command stops local supabase with no backup files.
```shell
make supa.down
```

## Development

### Start dev server
```shell
rye run uvicorn main:app --reload
```

Access to [Swager](http://localhost:8000/docs)
