import os
import datetime
import logging
import paramiko

from dotenv import load_dotenv
load_dotenv()


def _get_OpenERP_export_file_from_SFTP():
    transport = paramiko.Transport((os.getenv('FTP_ERP_HOST'), 22))
    transport.connect(username=os.getenv('FTP_ERP_LOGIN'), password=os.getenv('FTP_ERP_PASSWORD'))
    sftp = paramiko.SFTPClient.from_transport(transport)

    try:
        files = sftp.listdir(os.getenv('FTP_ERP_PATH'))
        dates = []
        for file in files:
            if file.startswith('LigneAFacturer'):
                parties = file.replace('LigneAFacturer', '').replace('.csv', '').split('_')
                date = datetime.datetime(int(parties[0]), int(parties[1]), int(parties[2]), int(parties[3]),
                                         int(parties[4]), int(parties[5]))
                dates.append((date, file))

        most_recent_file = max(dates, key=lambda x: x[0])[1]
        path_to_most_recent_file = f'/home/aol/Float/{most_recent_file}'
        sftp.get(os.path.join(os.getenv('FTP_ERP_PATH'), most_recent_file), path_to_most_recent_file)

        logging.info(f'The most recent OpenERP export ({most_recent_file}) has been downloaded from the FTP server.')

    except Exception as e:
        logging.error(f'Error while downloading the OpenERP export from the FTP server. Error: {e}')

    finally:
        sftp.close()
        transport.close()

    return path_to_most_recent_file

file = _get_OpenERP_export_file_from_SFTP()
print(os.getenv(file))