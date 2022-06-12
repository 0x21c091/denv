# A utility tool to create ``.env`` files

## Basic Usage

merge two or many files write to dump file `.env.denv`

```bash
python main.py -f .env -f .env.prod > .env.denv
```

```text
# .env

APP_ENV=local
USER=local_user
PASSWORD=local_pass
COMMON_FOO=foo
```

```text
# .env.prod

APP_ENV=prod
USER=prod_user
PASSWORD=prod_pass
PROD_BAR=bar
```

```text
# .env.denv

APP_ENV=prod
COMMON_FOO=foo
PASSWORD=prod_pass
PROD_BAR=bar
USER=prod_user
```

## Advanced Usage

merge two or many files and use `os env` write to dump file `.env.denv`

```bash
export PASSWORD=os_export_pass
python main.py -f .env -f .env.prod -e > .env.denv
```

```text
# .env.denv

APP_ENV=prod
COMMON_FOO=foo
PASSWORD=os_export_pass
PROD_BAR=bar
USER=moroz
```