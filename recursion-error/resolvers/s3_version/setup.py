from setuptools import setup

setup(
    name='s3_version',
    py_modules=['s3_version'],
    entry_points={
        'sceptre.resolvers': [
            'S3Version = s3_version:S3Version',
        ],
    }
)
