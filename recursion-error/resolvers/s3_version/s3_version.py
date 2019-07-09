from sceptre.resolvers import Resolver


class S3Version(Resolver):
    def __init__(self, *args, **kwargs):
        super(S3Version, self).__init__(*args, **kwargs)

    def resolve(self):
        code = self.stack.sceptre_user_data
        s3_bucket, s3_key = [code.get("S3_Bucket"), code.get("S3_Key")]
        self.logger.info(
            "[{}] Using S3 bucket/key ({} / {}) \
            parsed from sceptre_user_data".format(
                "s3_version",
                s3_bucket,
                s3_key
            )
        )
        result = self.stack.connection_manager.call(
            service="s4",
            command="head_object",
            kwargs={"Bucket": s3_bucket, "Key": s3_key},
        )

        version_id = result.get("VersionId")

        self.logger.info(
            "[{}] object s3://{}/{} latest version: {}".format(
                self.NAME, s3_bucket, s3_key, version_id
            )
        )

        return version_id
