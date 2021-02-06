
import logging, json
logger = logging.getLogger(__name__)

class Settings:
    def __init__(self, bot):
        logger.debug("Ayarlar Aktarılıyor...")
        try:
            with open("ayarlar.txt", "r") as f:
                settings = f.read()
                data = json.loads(settings)
                data = json.loads(settings)
                bot.setSettings(data['Host'],
                                data['Port'],
                                data['Channel'],
                                data['Nickname'],
                                data['Authentication'],
                                data["MessagesOnly"])
                logger.debug("Ayarlar Aktarıldı.")
        except ValueError:
            logger.error("Ayarlar Dosyasını Kontrol Et!")
            raise ValueError("Ayarlar Dosyasını Kontrol Et!")
        except FileNotFoundError:

            logger.error("Yeni oluşturulan ayarlar.txt dosyanızı düzeltin.")
            with open('ayarlar.txt', 'w') as f:
                standard_dict = {
                                    
                                    "Host": "irc.chat.twitch.tv",
                                    "Port": 6667,
                                    "Channel": "#<channel>", ## <channel> yerine log tutulacak kanal Örn: "elraenn" / başında "#" işareti bulunsun!
                                    "Nickname": "<name>", ## <name> yerine oatch key'ine ait nick
                                    "Authentication": "oauth:<auth>",
                                    "MessagesOnly": False
                                }
                f.write(json.dumps(standard_dict, indent=4, separators=(',', ': ')))
                raise ValueError("Yeni oluşturulan ayarlar.txt dosyanızı düzeltin.")
