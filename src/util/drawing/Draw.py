
async def line(self, x1: int, y1: int, x2: int, y2: int, type: int):
    line = []
    line.append({"x": 0, "y": 0, "type": type})
    line.append({"x": x1 - 1, "y": y1 - 1, "type": 2})
    line.append({"x": x1, "y": y1, "type": 0})
    line.append({"x": x2, "y": y2, "type": 0})
    line.append({"x": 0, "y": 0, "type": 1})
    return line    