from datetime import datetime,date
from decimal import Decimal
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework import status
  

class EmployeeView(APIView):
    
    def get(self, request, pk=None):
        try:
            if pk is None:
                employees = Employee.objects.all()
                serializer = EmployeeSerializer(employees,many=True)
                
                
                
                
            else:
                employee = Employee.objects.get(pk=pk)
                serializer = EmployeeSerializer(employee)
                
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Employee.DoesNotExist:
            return Response({'error': 'Employee not found.'}, 
                          status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, 
                          status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request, *args, **kwargs):
        try:
            data = request.data 
            serializer = EmployeeSerializer(data=data)
            

            if serializer.is_valid():
                
                serializer.save()
                return Response({'data': serializer.data, 'message': 'Employee Created Successfully'},
                                status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def put(self, request, pk):
        try:
            employee = Employee.objects.get(pk=pk)
            serializer = EmployeeSerializer(employee, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Employee.DoesNotExist:
            return Response({'error': 'Employee not found.'},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def patch(self, request, pk):
        try:
            employee = Employee.objects.get(pk=pk)
            serializer = EmployeeSerializer(employee, data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Employee.DoesNotExist:
            return Response({'error': 'Employee not found.'},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request, pk):
        try:
            employee = Employee.objects.get(pk=pk)
            employee.delete()
            return Response({'message': 'Employee deleted successfully'},status=status.HTTP_200_OK)
        except Employee.DoesNotExist:
            return Response({'error': 'Employee not found.'},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ManagerView(APIView):
    def get(self, request, pk=None):
        try:
            if pk is None:
                managers = Manager.objects.all()
                serializer = ManagerSerializer(managers, many=True)
            else:
                manager = Manager.objects.get(pk=pk)
                serializer = ManagerSerializer(manager)
            return Response(serializer.data)
        except Manager.DoesNotExist:
            return Response({'error': 'Manager not found.'},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request):
        try:
            serializer = ManagerSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def put(self, request, pk):
        try:
            manager = Manager.objects.get(pk=pk)
            serializer = ManagerSerializer(manager, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Manager.DoesNotExist:
            return Response({'error': 'Manager not found.'},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def patch(self, request, pk):
        try:
            manager = Manager.objects.get(pk=pk)
            serializer = ManagerSerializer(manager, data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Manager.DoesNotExist:
            return Response({'error': 'Manager not found.'},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request, pk):
        try:
            manager = Manager.objects.get(pk=pk)
            manager.delete()
            return Response({'message': 'Manager deleted successfully'},status=status.HTTP_204_NO_CONTENT)
        except Manager.DoesNotExist:
            return Response({'error': 'Manager not found.'},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
