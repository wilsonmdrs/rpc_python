from xmlrpc.server import SimpleXMLRPCServer


class RPC:
    _metodos_rpc = {'get', 'set', 'delete', 'veredito'}

    def __init__(self, direccion):
        self._data = {}
        self._servidor = SimpleXMLRPCServer(direccion, allow_none=True)

        for metodo in self._metodos_rpc:
            self._servidor.register_function(getattr(self, metodo))

    def veredito(self, name):
        if self._data.__len__() == 2:
            attr = []
            for testemunha in self._data:
                attr.append(testemunha)
            if self._data[attr[0]] == 'sim' and self._data[attr[1]] == 'sim':
                return name + ' recebeu 5 anos de Prisão'
            if self._data[attr[0]] == 'não' and self._data[attr[1]] == 'não':
                return name + ' recebeu 3 Anos de Prisão'
            if self._data[attr[0]] == 'sim' and self._data[attr[1]] == 'não' and attr[0] == name:
                return name + ' Está Solto'
            if self._data[attr[0]] == 'sim' and self._data[attr[1]] == 'não' and attr[1] == name:
                return name + ' recebeu 10 Anos de Prisão'
            if self._data[attr[0]] == 'não' and self._data[attr[1]] == 'sim' and attr[0] == name:
                return name + ' recebeu 10 Anos de Prisão'
            if self._data[attr[0]] == 'não' and self._data[attr[1]] == 'sim' and attr[1] == name:
                return name + ' Está  Solto'
            if self._data[attr[0]] == 'sim' and self._data[attr[1]] == 'sim':
                return name + ' recebeu 5 anos de Prisão'
        else:
            return 'Aguardando Veredito para ' + name

    def get(self, name):
        return self._data[name]

    def set(self, name, response):
        if self._data.__len__() < 2:
            self._data[name] = response
        else:
            self._data = {}
            self._data[name] = response

    def delete(self, name):
        del self._data[name]

    def iniciar_servidor(self):
        self._servidor.serve_forever()


if __name__ == '__main__':
    rpc = RPC(('', 20064))
    print('Starting Server RPC.')
    rpc.iniciar_servidor()
