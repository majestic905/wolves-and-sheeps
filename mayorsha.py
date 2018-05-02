from template import generate

name = 'mayorsha'
data = """\
[[['авдотья ивановна'],
  ['авдотья ивановна', 'карягина'],
  ['авдотья ивановна', 'карягина', 'феня'],
  ['авдотья ивановна', 'карягина'],
  ['авдотья ивановна', 'архип'],
  ['архип', 'феня'],
  ['авдотья ивановна', 'феня'],
  ['авдотья ивановна', 'феня', 'терихов'],
  ['авдотья ивановна', 'карягина', 'иван'],
  ['авдотья ивановна', 'карягин', 'карягина'],
  ['авдотья ивановна', 'карягин', 'карягина', 'иван']],
 [['любавин'],
  ['любавин', 'терихов', 'феня'],
  ['любавин', 'терихов', 'феня', 'архип'],
  ['архип', 'терихов', 'феня'],
  ['терихов', 'сладнев'],
  ['терихов', 'сладнев', 'феня'],
  ['терихов', 'сладнев', 'феня', 'карягин'],
  ['феня', 'карягин'],
  ['карягин', 'сладнев'],
  ['сладнев', 'терихов'],
  ['сладнев', 'терихов', 'анна захаровна'],
  ['сладнев', 'терихов', 'анна захаровна', 'феня'],
  ['терихов', 'феня'],
  ['терихов', 'архип', 'волжин']],
 [['карягина', 'пров'],
  ['карягин', 'карягина'],
  ['карягин', 'карягина', 'феня', 'любавин'],
  ['феня', 'карягин', 'волжин'],
  ['феня', 'карягина'],
  ['феня', 'карягина', 'карягин'],
  ['карягин', 'волжин', 'пров', 'иван', 'карягина'],
  ['карягин', 'волжин', 'карягина', 'феня', 'авдотья ивановна']],
 [['волжин', 'архип'],
  ['волжин', 'анна захаровна'],
  ['волжин', 'анна захаровна', 'терихов'],
  ['волжин', 'терихов'],
  ['феня', 'сладнев'],
  ['феня', 'волжин'],
  ['волжин', 'архип', 'терихов', 'феня'],
  ['терихов', 'сладнев'],
  ['терихов', 'сладнев', 'феня'],
  ['феня', 'терихов'],
  ['терихов', 'архип'],
  ['архип', 'карягин', 'феня']],
 [['пров', 'иван'],
  ['пров', 'иван', 'карягин'],
  ['карягин'],
  ['карягин', 'феня'],
  ['карягин', 'карягина', 'феня']]]
"""

generate(name, data)