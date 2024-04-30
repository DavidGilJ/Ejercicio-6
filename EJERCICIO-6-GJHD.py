def capturar_ladrones(arr, k):
  n = len(arr)  
  capturados = 0
  i = 0

  while i < n:
      if arr[i] == 'P':
        
          j = max(0, i - k)
          while j < min(n, i + k + 1):
              if arr[j] == 'L':
                  capturados += 1
                  arr[j] = 'C'  
                  break
              j += 1
          if j == min(n, i + k + 1):
            
              j = max(0, i - k)
              while j < i:
                  if arr[j] == 'L':
                      capturados += 1
                      arr[j] = 'C' 
                      break
                  j += 1
      i += 1

  return capturados

# Ejemplo 1
arr = ['P', 'P', 'P', 'L', 'P', 'L', 'P', 'L', 'L', 'L']
k = 1

# Ejemplo 2
#arr = ['L', 'L', 'L', 'P', 'P', 'L', 'P', 'P', 'P', 'L']
#k = 2
capturados = capturar_ladrones(arr, k)
print("Cantidad de ladrones capturados:", capturados)
