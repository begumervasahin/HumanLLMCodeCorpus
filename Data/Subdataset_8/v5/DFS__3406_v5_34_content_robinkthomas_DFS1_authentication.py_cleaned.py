import re
import base64
import shelve
import web
urls = ('/', 'Index')
class Index:
    def GET(self):
        auth_header = web.ctx.env.get('HTTP_AUTHORIZATION')
        if auth_header is None:
            return self.send_unauthorized_response()
        else:
            try:
                username, password = self.extract_credentials(auth_header)
                if self.authenticate_user(username, password):
                    return "Authorized!"
                else:
                    return "Not Authorized!"
            except Exception as e:
                print("Error:", e)
                return "Not Authorized!"
    def send_unauthorized_response(self):
        web.header('WWW-Authenticate', 'Basic realm="Auth example"')
        web.ctx.status = '401 Unauthorized'
        return "Not Authorized!"
    def extract_credentials(self, auth_header):
        auth_token = re.sub('^Basic ', '', auth_header)
        username, password = base64.b64decode(auth_token.encode()).decode().split(':')
        return username, password
    def authenticate_user(self, username, password):
        try:
            with shelve.open("login.dat") as db:
                stored_password = db.get(username)
                if stored_password and password == stored_password:
                    return True
        except Exception as e:
            print("Error:", e)
        return False
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run(port=8083)