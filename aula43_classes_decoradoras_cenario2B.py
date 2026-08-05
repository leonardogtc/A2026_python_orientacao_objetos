"""
Exemplo 2: Registrador de Classes (Padrão de Projeto Registry)
Outra aplicação muito comum é registrar classes automaticamente quando o arquivo
é importado (muito usado em frameworks web como Flask/Django ou engines de jogos)
"""

CLASSES_REGISTRADAS = {}


def registrar_plugin(cls):
    # Adiciona a classe a um dicionário global usando o nome como chave
    CLASSES_REGISTRADAS[cls.__name__] = cls
    return cls


@registrar_plugin
class PluginPDF:
    def exportar(self):
        return "Exportando PDF..."


@registrar_plugin
class PluginExcel:
    def exportar(self):
        return "Exportando Excel..."


# As classes foram registradas automaticamente:
print(CLASSES_REGISTRADAS)
# Saída: {'PluginPDF': <class '__main__.PluginPDF'>, 'PluginExcel': <class '__main__.PluginExcel'>}
