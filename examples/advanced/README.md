# Mealie
export MEALIE_DOMAIN=mealie.localhost

helmfile --file mealie.yaml apply

user: changeme@email.com
pass: MyPassword

Create admin token

export MEALIE_TOKEN=

Enable cronjob

# Joplin

export JOPLIN_PG_PASS=userpass
export JOPLIN_PG_POSTGRESPASS=adminpass
export JOPLIN_DOMAIN=joplin.localhost

helmfile --file joplin.yaml apply
