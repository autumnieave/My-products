#pragma once
#include<iostream>
#include<vector>
using namespace std;
template <unsigned int N>
class Array {
public:
	template<unsigned int N>
	friend Array<N> operator*(double lhs, const Array<N>& rhs);
	Array(initializer_list<double> rhs) {
		auto p = rhs.begin();
		for (int i = 0; i < N; i++) {
			list[i] = *(p++);
		}
	};
	Array() {};
	explicit Array(double rhs[]) {
		for (int i = 0; i < N; i++) {
			list[i] = rhs[i];
		}
	}
	~Array() {};
	Array(const Array<N>& rhs) {
		for (int i = 0; i < N; i++) {
			list[i] = rhs.list[i];
		}
	}
	void operator=(const Array<N>& rhs) {
		for (int i = 0; i < N; i++) {
			list[i] = rhs.list[i];
		}
	}
	void show() {
		for (int i = 0; i < N; i++) {
			cout << (list[i]) << " ";
		}
		cout << endl;
	}
	double operator[](int i)const {
		return list[i];
	}
	double& operator[](int i) {
		double s = list[i];
		return s;
	}
	Array operator+(const Array<N>& rhs)const {
		double mid[N];
		for (int i = 0; i < N; i++) {
			mid[i] = list[i];
		}
		for (int i = 0; i < N; i++) {
			mid[i] += rhs.list[i];
		}
		Array r(mid);
		return r;
	}
	Array operator-(const Array<N>& rhs) {
		double mid[N];
		for (int i = 0; i < N; i++) {
			mid[i] = list[i];
		}
		for (int i = 0; i < N; i++) {
			mid[i] -= rhs.list[i];
		}
		Array r(mid);
		return r;
	}
	Array operator*(double rhs)const {
		double mid[N];
		for (int i = 0; i < N; i++) {
			mid[i] = rhs * list[i];
		}
		Array r(mid);
		return r;
	}
	double operator*(const Array<N>& rhs) const {
		double mid[N];
		double sum = 0;
		for (int i = 0; i < N; i++) {
			mid[i] = list[i];
		}
		for (int i = 0; i < N; i++) {
			mid[i] *= rhs.list[i];
			sum += mid[i];
		}
		return sum;
	}
private:
	double list[N];
};
template<unsigned int N>
Array<N> operator*(double lhs, const Array<N>& rhs) {
	double mid[N];
	for (int i = 0; i < N; i++) {
		mid[i] = lhs * rhs.list[i];
	}
	Array<N> r(mid);
	return r;
}