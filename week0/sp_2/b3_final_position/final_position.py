def final_position(commands, A, B):
  position = 0 #zapochwame ot poziciq 0
  for cmd in commands: #obhojdame stringa s komandi
    if cmd == 'R' and position < B: #ako sme predi poziciq B, mestim nadqsno
      position += 1
    elif cmd == 'L' and position > -A: #ako sme prezi poziciq -A, mestim nalqvo
      position -= 1
  return position
