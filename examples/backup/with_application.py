import squarecloud as square

client = square.Client(api_key='API KEY')


async def example():
    app = await client.app('application_id')
    backup = await app.backup()
    print(backup.downloadURL)  # https://squarecloud.app/dashboard/backup/f.zip
