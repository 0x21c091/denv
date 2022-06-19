# A utility tool to create ``.env`` files

## Basic Usage

merge two or many files write to dump file `.env.denv`

```bash
python main.py -f .env -f .env.prod > .env.denv
```

`.env`

```text
APP_ENV=local
USER=local_user
PASSWORD=local_pass
COMMON_FOO=foo
```

`.env.prod`

```text
APP_ENV=prod
USER=prod_user
PASSWORD=prod_pass
PROD_BAR=bar
```

`.env.denv`

```text
APP_ENV=prod
COMMON_FOO=foo
PASSWORD=prod_pass
PROD_BAR=bar
USER=prod_user
```

## Advanced Usage

merge two or many files and use `os env` with strict mode write to dump file `.env.denv`

```bash
export PASSWORD=os_export_pass
python main.py -f .env -f .env.prod -e -es > .env.denv
```

`.env.denv`

```text
APP_ENV=prod
COMMON_FOO=foo
PASSWORD=os_export_pass
PROD_BAR=bar
USER=moroz
```