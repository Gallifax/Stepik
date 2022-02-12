# Прогуливаясь по Манхэттену, вы не можете попасть из точки А в точку Б по кратчайшему пути.
# Если только вы не умеете проходить сквозь стены, вам обязательно придется идти вдоль его параллельно-перпендикулярных улиц.

#На плоскости манхэттенское расстояние между двумя точками определяется так |p_{1}-q_{1}|+|p_{2}-q_{2}|∣

# Напишите программу определяющую манхэттенское расстояние между двумя точками, координаты которых заданы.

p1, p2, q1, q2 = int(input()), int(input()), int(input()), int(input())
print(abs(p1 - q1) + abs(p2 - q2))
