# supa: Supabase Commands

supa.setup:
	brew install supabase/tap/supabase

supa.update:
	brew upgrade supabase

supa.up:
	supabase start

supa.down:
	supabase stop --no-backup

supa.login:
	supabase login
