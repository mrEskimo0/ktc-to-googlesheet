cd %USERPROFILE%\ktc_to_googlesheet-master
python ktc_to_googlesheet.py

IF %ERRORLEVEL% EQU 1 GOTO senderror1
EXIT

:senderror1
python send_email.py