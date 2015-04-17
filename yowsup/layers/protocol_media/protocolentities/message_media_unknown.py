from yowsup.structs import ProtocolEntity, ProtocolTreeNode
from .message_media import MediaMessageProtocolEntity

class UnknownMediaMessageProtocolEntity(MediaMessageProtocolEntity):


    def __init__(self, mediatype, _id = None, _from = None, to = None, notify = None, timestamp = None, participant = None,
            preview = None, offline = None, retry = None):

        super(UnknownMediaMessageProtocolEntity, self).__init__("unknown", _id, _from, to, notify, timestamp, participant, preview, offline, retry)
        self.setVcardMediaProps(mediatype)

    def __str__(self):
        out  = super(MediaMessageProtocolEntity, self).__str__()
        out += "Name: %s\n" % self.name
        return out

    def getType(self):
        return self.mediatype

    def getCardData(self):
        return self.card_data
   
    def setVcardMediaProps(self, mediatype):
        self.mediatype = mediatype

    def toProtocolTreeNode(self):
        node = super(UnknownMediaMessageProtocolEntity, self).toProtocolTreeNode()
        mediaNode = node.getChild("media")
        mediaNode["type"] = "unknown"
        vcardNode = ProtocolTreeNode("unknown", {"name":self.name}, None,self.card_data)
        mediaNode.addChild(vcardNode)
        return node

    @staticmethod
    def fromProtocolTreeNode(node):
        entity = MediaMessageProtocolEntity.fromProtocolTreeNode(node)
        entity.__class__ = UnknownMediaMessageProtocolEntity
        mediaNode = node.getChild("media")
        entity.setVcardMediaProps(
            mediaNode.getAttributeValue('type')
        )
        return entity
