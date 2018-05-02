from template import generate

name = 'mertvaya_petlya'
data = """\
[[['крамолина', 'слуга'],
  ['крамолина', 'кокуркина', 'слуга'],
  ['крамолина', 'лопырев', 'слуга'],
  ['вермутская', 'крамолина', 'лопырев', 'слуга'],
  ['вермутская', 'крамолина', 'слуга'],
  ['крамолина', 'кокуркина'],
  ['крамолина', 'чаганов', 'слуга'],
  ['слетышев', 'кокуркина', 'слуга'],
  ['слетышев'],
  ['крамолина', 'слетышев'],
  ['крамолина', 'слетышев', 'вермутская'],
  ['крамолина', 'слетышев', 'вермутская', 'лопырев', 'слуга']],
 [['вера', 'дуня'],
  ['вера', 'дуня', 'пырешева', 'дементий'],
  ['пырешева', 'запольев'],
  ['запольев', 'вера', 'дементий'],
  ['запольев', 'чаганов'],
  ['запольев', 'чаганов', 'вера'],
  ['запольев', 'чаганов', 'вера', 'пырешева', 'дементий'],
  ['дементий', 'слетышев'],
  ['слетышев', 'чаганов']],
 [['чаганов', 'муравин', 'громчевский', 'кинин'],
  ['чаганов', 'муравин', 'громчевский', 'кинин', 'слетышев'],
  ['чаганов', 'муравин', 'громчевский', 'кинин', 'слетышев', 'василий'],
  ['слетышев', 'чаганов', 'муравин'],
  ['муравин', 'слетышев'],
  ['муравин', 'слетышев', 'паганов'],
  ['муравин', 'слетышев', 'паганов', 'василий', 'вера'],
  ['слетышев', 'кинин', 'громчевский'],
  ['слетышев', 'кинин', 'громчевский', 'чаганов', 'вера', 'муравин'],
  ['слетышев', 'кинин', 'громчевский', 'чаганов', 'вера', 'муравин', 'крамолина']],
 [['катя', 'вера'],
  ['кинин', 'вера'],
  ['кинин', 'катя', 'запольев'],
  ['запольев', 'вера'],
  ['вера', 'катя', 'чаганов'],
  ['чаганов', 'слетышев'],
  ['слетышев', 'вера']],
 [['крамолина', 'кинин'],
  ['крамолина', 'кокуркина', 'слуга'],
  ['крамолина', 'лопырев'],
  ['крамолина', 'слуга'],
  ['крамолина', 'вермутская', 'кокуркина', 'слуга'],
  ['кокуркина', 'слуга'],
  ['кокуркина', 'чаганов', 'слуга'],
  ['чаганов', 'крамолина', 'вера', 'слетышев', 'слуга'],
  ['чаганов', 'крамолина', 'вера', 'слетышев', 'слуга', 'околодочный']]]
"""

generate(name, data)