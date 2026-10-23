# Database-migration acceptance tests

Run these tests by naming this hidden directory explicitly:

```sh
python3 -m unittest discover -s .referee/003-database-migration -p 'test_*.py' -v
```

The suite assesses only the documentation deliverables required by the work
order. It does not inspect or execute application implementation code: the
approved destination and executable migration design are intentionally outside
the current evidence-bounded plan.
