from my_clis import create_run_clis

try:
    create_run_clis()
except KeyboardInterrupt:
    print('\nExit with "Ctrl+c"')
